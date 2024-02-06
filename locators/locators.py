class LoginPageLocators:
    log_in_menu_xpath = "(//span[@class='hidden-on-mobile'])[1]"
    log_off_menu_xpath = "//span[@class='helper-text hidden-on-mobile']"



    to_login_page_link_text = "Zaloguj się"
    logoff_check_link_text = "Wyloguj"

    email_input_css = "input[name='email']"
    password_input_css = "input[name='password']"
    button_css = "button[value='submit']"

    error_msg_popup_css = "div[class='swal2-modal swal-shop-action-popup show-swal2'] h2"
    popup_close__css = "button[type='button'] a"

    blank_error_css = ".fa.fa-exclamation"

class ProductSearchLocators:

    search_input_xpath = "//input[@cy-data='headerSearch']"
    search_result_check_css = "h1[class='title']"

    dropdown_tag_name = "select"
    search_order_page = "https://printshop-24.pl/category/sort/price/?q="

class UserAccountLocators:

    accountlink_link_text = "Twoje konto"
    edit_account_link_text = "Edycja danych"

    user_firstname_css = "input[name='user_firstname']"
    user_lastname_css = "input[name='user_lastname']"
    user_phone_css = "input[name='user_phone']"
    dropbox_menu_xpath = "(//span[@role='presentation'])[1]"
    textbox_css = "input[role='textbox']"
    user_city_css = "input[name='user_city']"
    user_street_css = "input[name='user_street']"
    user_code_css = "input[name='user_code']"

    submit_button_css = "button[value='submit']"

    phone_check_xpath = "(//span[@class='text-field'])[3]"
    name_check_xpath = "(//span[@class='text-field'])[4]"
    adress_check_xpath = "(//span[@class='text-field'])[5]"

class ShoppingCartLocators:

    menu_link_text = "MENU"
    menu_pillow_xpath = "//ul[@class='header_bottom_content_list']//a[contains(text(),'PODUSZKI NA DZIEŃ MAMY')]"

    pillow_content_xpath = "img[alt='PODUSZKA DLA NAJFAJNIEJSZEJ MAMY']"

    increasing_Cart_css = ".fa.fa-plus"

    add_to_cart_css = ".add-to-cart.core_addToCart"
    click_basket_icon_css = "a[class='header_middle_content_quick_cart'] i[class='fa fa-shopping-basket']"
    cart_item_quantity_css = "div[class='header_middle_content_quick_cart_counter counter'] span[class='core_quickCartAmount']"

    tile_css = "img[alt='kubek z nadrukiem']"
    product_css = "(//img[@alt='KUBEK Z NADRUKIEM: TWOIM ZDJĘCIEM, NAPISEM, GRAFIKĄ'])[1]"
    remove_basket_css = "tbody tr:nth-child(2) td:nth-child(8) i:nth-child(1)"
    ok_remove_button_css = "button[class='swal2-confirm btn styled']"
    remove_info_xpath = "//div[@class='cart-empty ']"


