---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Focused]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 1400}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *dragon rune bracelet* is a gold bangle formed around the scale of a famous dragon. The bracelet is etched with esoteric symbols or words in Draconic that indicate kinship with dragons. As many types of *dragon rune bracelet* exist as there are types of dragons, though bracelets associated with uncommon or rare dragons have the same rarity as the dragon.

While wearing a *dragon rune bracelet*, you gain a +2 item bonus to Diplomacy checks while interacting with dragons of the same type as the bracelet's scale (such as red dragons or cloud dragons). You also gain a +2 item bonus to saving throws against fear effects from any kind of dragon.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can spend only to cast a sorcerer draconic bloodline spell. If not used by the end of your turn, this Focus Point is lost.

**Craft Requirements** You are a sorcerer of a draconic bloodline.

**Source:** `= this.source` (`= this.source-type`)
