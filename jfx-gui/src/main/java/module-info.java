module org.ibtc.ibtc {
    requires javafx.controls;
    requires javafx.fxml;

    opens org.ibtc.ibtc to javafx.fxml;
    exports org.ibtc.ibtc;
}