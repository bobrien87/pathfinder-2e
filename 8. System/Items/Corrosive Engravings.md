---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Acid]]", "[[Grimoire]]", "[[Magical]]"]
price: "{'gp': 140}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These tin sheets are bound in brass and show significant signs of erosion. The grimoire's title is acid-etched, and flipping between the sheets leaves your fingers covered in flecks of rust and powdery metal.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** If your next action is to cast an acid or poison spell that deals persistent damage, any creature who takes persistent damage from the spell is also [[Sickened]] 2 until the persistent damage ends. Using an action to retch can reduce the sickened value as normal, but it can't reduce the sickened value below 1 until the persistent damage ends.

**Source:** `= this.source` (`= this.source-type`)
