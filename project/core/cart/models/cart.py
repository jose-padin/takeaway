from django.db import models


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="related product"
    )
    order_id = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="related order"
    )

    