package org.ctf.ho9na.Controller;

import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceException;
import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import jakarta.servlet.http.HttpSession;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import java.util.List;

@Controller
public class MainController {
    @Autowired
    private EntityManager entityManager;

    @GetMapping("/")
    public ModelAndView index(HttpSession httpSession) {
        ModelAndView modelAndView = new ModelAndView("index");
        if (httpSession.getAttribute("username") == null) {
            modelAndView.setViewName("redirect:/login");
            return modelAndView;
        }
        return modelAndView;
    }

    @GetMapping("/login")
    public String login() {
        return "login";
    }

    @GetMapping("/register")
    public String register() {
        return "register";
    }

    @PostMapping("/login")
    public ModelAndView login(@RequestParam String username, @RequestParam String password, HttpSession httpSession, RedirectAttributes redirectAttributes) {
        String query = "SELECT username, password FROM awaba WHERE username = ? and password = ?";
        List < Object[] > resultList = entityManager.createNativeQuery(query)
                .setParameter(1, username)
                .setParameter(2, password)
                .getResultList();
        ModelAndView modelAndView = new ModelAndView("login");
        if (!resultList.isEmpty()) {
            httpSession.setAttribute("username", username);
            modelAndView.setViewName("redirect:/");
            return modelAndView;
        } else {
            modelAndView.addObject("error", "Login impermiable hbibi");
            return modelAndView;
        }
    }

    @PostMapping("/register")
    @Transactional
    public ModelAndView register(@RequestParam String username, @RequestParam String password, RedirectAttributes redirectAttributes) {
        String queryCheck = "SELECT COUNT(*) FROM awaba WHERE username = ?";

        ModelAndView modelAndView = new ModelAndView("register");

        Object result = entityManager.createNativeQuery(queryCheck)
                .setParameter(1, username)
                .getSingleResult();

        int count = ((Number) result).intValue();

        if (count > 0) {
            modelAndView.addObject("error", "rah 9olnalk impermiable a hbibi change username.");
            return modelAndView;
        }

        // Proceed with registration since username is not duplicate
        String queryInsert = "INSERT INTO awaba (username, password) VALUES (?, ?)";
        int rowsAffected = entityManager.createNativeQuery(queryInsert)
                .setParameter(1, username)
                .setParameter(2, password)
                .executeUpdate();

        if (rowsAffected > 0) {
            modelAndView.setViewName("redirect:/login");
            return modelAndView;
        } else {
            modelAndView.addObject("error", "Login impermiable hbibi.");
            return modelAndView;
        }
    }

    @GetMapping("/mola7ada")
    public ModelAndView displayNotePage(@RequestParam String name, HttpSession httpSession) {

        ModelAndView modelAndView = new ModelAndView("note");
        if (httpSession.getAttribute("username") == null) {
            modelAndView.setViewName("redirect:/login");
            return modelAndView;
        }
        return modelAndView;
    }
}
