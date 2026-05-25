---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]", "[[Tea]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This green tea is often steeped in a pot with a dried persimmon. Traditionally, all participants in a complex discussion start their conversation with a tea ceremony involving *covenant tea*, with each member of the group enjoying the covenant of the shared beverage. Some have been known to use trickery and sleight of hand to ensure that only those whose goals align with the tea preparer's are served covenant tea, while others in the group are served non-magical (but still delicious) green tea, thus subtly tipping the balance in discussion toward those the tea server favors. This practice has resulted in some regions referring to *covenant tea* as "trickery tea." Regardless of what you prefer to call the tea, when you drink it, you gain a +1 item bonus to Diplomacy checks and to your Perception DC for 10 minutes.

> [!danger] Effect: Covenant Tea

**Activate—Tea Ceremony** 10 minutes (concentrate, manipulate) The duration increases to 1 hour.

**Source:** `= this.source` (`= this.source-type`)
