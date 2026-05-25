---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Focused]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 1200}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Dangling from a simple cord, a hexing jar houses rich soil. When a witch who has invested the jar wears it overnight, a miniature thing grows from the soil. Your patron chooses the form, commonly including glowing mushrooms, venus flytraps, mandragora roots, or undead hands reaching up. The thing whispers secrets it learned from your patron, giving you a +2 item bonus to your patron skill.

**Activate** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** You gain 1 Focus Point, which you can use only to cast a witch hex spell. If not used by the end of your turn, this Focus Point is lost.

**Activate** R (concentrate)

**Frequency** once per hour

**Trigger** You roll a critical success on an attack roll with a witch spell, or your target rolls a critical failure on its saving throw against a witch spell or hex you cast

**Effect** The thing in the jar becomes more energetic—glowing, dancing, rapping on the glass, or some other action appropriate to its appearance. It encourages you until the start of your next turn, granting you and your familiar a +1 status bonus to AC and saving throws and a +2 status bonus against mental effects.

> [!danger] Effect: Hexing Jar

**Craft Requirements** You are a witch.

**Source:** `= this.source` (`= this.source-type`)
