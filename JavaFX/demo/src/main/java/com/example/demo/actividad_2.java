package com.example.demo;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;

import java.io.IOException;

public class actividad_2 extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        MenuBar menu = new MenuBar();

        Label texto = new Label("Scene 1");
        texto.setPadding(new Insets(15, 0, 0, 0));

        Menu opciones = new Menu("Opciones");
        MenuItem scene1 = new MenuItem("Scene 1");
        MenuItem scene2 = new MenuItem("Scene 2");
        opciones.getItems().addAll(scene1,scene2);

        menu.getMenus().add(opciones);
        scene2.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                scene2();
            }
        });


        VBox vBox = new VBox();
        vBox.getChildren().addAll(menu, texto);

        stage.setTitle("Transicion menus");

        Scene scene = new Scene(vBox, 300,300);

        stage.setScene(scene);

        stage.show();

    }
    public void scene2(){
        Stage newStage = new Stage();
        VBox newVbox = new VBox();
        Label newTexto = new Label("Scene 2");
        newTexto.setPadding(new Insets(10,0,0,0));

        MenuBar menu1 = new MenuBar();


        Menu opciones1 = new Menu("Opciones");
        MenuItem scene1 = new MenuItem("Scene 1");
        MenuItem scene2 = new MenuItem("Scene 2");
        opciones1.getItems().addAll(scene1,scene2);

        newStage.setTitle("Transicion menus");

        scene1.setOnAction(new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                newStage.close();
            }
        });

        menu1.getMenus().add(opciones1);


        Scene newScene = new Scene(newVbox, 300,300);
        newVbox.getChildren().addAll(menu1, newTexto);

        newStage.setScene(newScene);
        newStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}