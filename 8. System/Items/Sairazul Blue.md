---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Earth]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 180}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A *Sairazul blue* potion is a rich navy blue in color. Subjects of the Crystalline Queen produced the potion to protect themselves from the radiation Ayrzul left behind. For the next 8 hours, your skin becomes navy blue, and you gain resistance 5 to poison damage and void damage.

> [!danger] Effect: Sairazul Blue

If you drop to 0 Hit Points due to poison or void damage, the *Sairazul blue* within your body reacts, healing you for 8d8 healing Hit Points. The resistances the potion grants then end.

**Source:** `= this.source` (`= this.source-type`)
