---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 800}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You succeed at a Strike with the affixed weapon.

This imposing fang is engraved with an intricate arrangement of symbols, glyphs, and patterns and dangles from a leather strap bound to the hilt of the affixed weapon. When you Activate the trophy, your weapon is momentarily transformed into a magical construct of draconic fury. On the triggering Strike and until the end of your next turn, the damage type of the affixed weapon changes to the type matching the dragon the claw came from. This change overrides the versatile trait and similar abilities.

**Craft Requirements** Supply one tooth from an adult or older dragon.

**Source:** `= this.source` (`= this.source-type`)
