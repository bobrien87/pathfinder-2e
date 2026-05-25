---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 15}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Journeybread contains a mix of fruits, nuts, and grains with an alchemical boost. Eating one journeybread provides all the food and water you need for a day. If you subsist on nothing else for a week, you become temporarily immune to journeybread until you eat real food and drink water normally for 24 hours.

In addition to the benefits of journeybread, power journeybread grants you a +1 item bonus to Athletics checks to [[Climb]], [[Force Open]], and [[Swim]], and to Fortitude saving throws against being sickened. The number of minutes you can [[Hustle]] changes to your Constitution modifier × 20. These benefits last for 4 hours.

> [!danger] Effect: Journeybread (Power)

**Source:** `= this.source` (`= this.source-type`)
