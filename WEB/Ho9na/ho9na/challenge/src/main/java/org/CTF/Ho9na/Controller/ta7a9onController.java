package org.ctf.ho9na.Controller;

import jakarta.persistence.EntityManager;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import jakarta.servlet.http.HttpSession;

@RestController
@RequestMapping("/api")
public class ta7a9onController {
    @Autowired
    private EntityManager entityManager;
    @GetMapping("/mola7adat")
    public ResponseEntity < ? > notes(HttpSession httpSession) {
        if (httpSession.getAttribute("username") == null) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("unauthorized");
        }
        String query = "Select * from mola7adat";
        List < Object[] > resultList = entityManager.createNativeQuery(query).getResultList();
        List < Map < String, Object >> result = new ArrayList < > ();
        for (Object[] row: resultList) {
            Map < String, Object > rowMap = new HashMap < > ();
            rowMap.put("ID", row[0]);
            rowMap.put("Note", row[1]);
            rowMap.put("mola7ada", row[2]);
            result.add(rowMap);
        }
        return ResponseEntity.ok(result);
    }

    @PostMapping("/mola7ada")
    public ResponseEntity<?> noteByName(@RequestParam String name, HttpSession httpSession) {
        if (httpSession.getAttribute("username") == null) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("unauthorized");
        }

        // Vulnerable query: Directly concatenates user input
        String query = String.format("Select * from mola7adat where name ='%s'", name);
        List<Object[]> resultList = entityManager.createNativeQuery(query).getResultList();
        List<Map<String, Object>> result = new ArrayList<>();
        for (Object[] row : resultList) {
            Map<String, Object> rowMap = new HashMap<>();
            rowMap.put("ID", row[0]);
            rowMap.put("Name", row[1]);
            rowMap.put("mola7ada", row[2]);
            result.add(rowMap);
        }

        return ResponseEntity.ok(result);
    }
}
