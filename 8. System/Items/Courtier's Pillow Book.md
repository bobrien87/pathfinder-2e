---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This elegant journal has a detailed social dossier on the owner's acquaintances. When you make your daily preparations, you can inscribe a secret or embarrassing foible about a specific individual that you know to be true or have on good authority.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** If your next action is to cast a mental spell on a target about whom you've written an entry in the book, you can state that secret or foible before Casting the Spell to give the target a –1 circumstance penalty to their saving throw against the spell. The inscription then disappears from the grimoire.

**Source:** `= this.source` (`= this.source-type`)
