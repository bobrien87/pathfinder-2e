---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 11}"
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

Shaped like a pointed, gnarled finger on a stick, witch's finger is a frozen treat imbued with berries that lend it a blood-red hue. A popular tale claims Irriseni winter witches created this dessert, but the story is apocryphal; an enterprising ice cream shop owner in New Stetven invented the treat and, as a marketing ploy, the myth surrounding it. Taking a bite makes you feel warm. For 1 hour, you have cold resistance 3, and for 8 hours, the treat negates the damage you would take from severe environmental cold and reduces the damage you take from extreme cold to that of severe cold.

> [!danger] Effect: Witch's Finger

**Source:** `= this.source` (`= this.source-type`)
