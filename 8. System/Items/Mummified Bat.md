---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 175}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (concentrate)

This talisman is the magically treated corpse of a tiny bat bound in papyrus. When activated, the affixed weapon detects vibrations around you and guides your perception. For 1 minute, you don't need to succeed at a flat check to target [[Concealed]] creatures. You're not [[Off Guard]] to creatures that are [[Hidden]] from you (unless you're off-guard to them for reasons other than the hidden condition), and you need only a successful DC 5 flat check to target a hidden creature. While you're adjacent to an undetected creature of your level or lower, it's instead only hidden from you.

If you have the [[Blind Fight]] feat, you gain imprecise echolocation with a range of 30 feet for 1 minute. This makes creatures that would be undetected by you because you can't see them hidden instead.

> [!danger] Effect: Mummified Bat

**Source:** `= this.source` (`= this.source-type`)
