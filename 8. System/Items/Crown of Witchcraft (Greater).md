---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Focused]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 21000}"
usage: "wornheadwear"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

An elegant accoutrement for a witch who has come into the higher echelons of power, a *crown of witchcraft* typically looks like a garland of flowering twigs, a jeweled circlet, or a tall hat of fine fabric. You gain a +2 item bonus to Intimidation checks, and if you're a witch, you gain a +3 item bonus to your patron skill.

If you have a familiar, you can attach a small portion of the crown's material to your familiar, such as a strip of fabric from a hat tied around its tail or a sprig of natural material linked to its collar; the familiar doesn't need to invest the item itself. If you do this, your familiar gains the tough pet ability as long as the crown is invested by you.

**Activate—Defiant Hex** `pf2:f` (concentrate)

**Frequency** once per day

**Effect** Gain 1 Focus Point, which you can spend only to cast a witch hex spell. If you don't spend this point by the end of this turn, it is lost.

**Craft Requirements** You are a witch.

**Source:** `= this.source` (`= this.source-type`)
