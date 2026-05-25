---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 50}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This thick syrup sweetens potions and creates a distinctive, metallic flavor associated with the festival days in Dhuraxilis. Partygoers are fond of mixing *soldier's syrup* with potions to extend their release.

Activating a dose of *soldier's syrup* requires you to combine it with another consumable potion that takes 1 action to activate. After swirling the mixture for a few moments, you must either imbibe the augmented potion within 1 minute, or the potion reverts to its unaugmented state. The potion's level cannot exceed that of the *soldier's syrup* it is mixed with, otherwise the syrup is wasted.

When consumed, a *soldier's syrup*–augmented potion does not immediately grant its benefits to you. Instead, you can activate the potion within the next hour as a single action, which has the concentrate trait. You can have only one *soldier's syrup*–augmented potion consumed at a time; consuming a second one renders the first one inert. If you do not activate the potion within 1 hour, the potion spoils inside you, and you become [[Enfeebled]] 1 for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
