---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Fortune]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 650}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Despite covering the entire face, this alabaster mask does not hinder vision or other senses. Wearing the mask grants a +2 item bonus to Performance checks while acting, orating, performing comedy, or singing.

**Activate—Assume Role** A (concentrate)

**Effect** You change the mask's appearance into an artistic rendition of a dramatic character of your choice.

**Activate—Sacrifice Role** R (concentrate, fortune)

**Frequency** once per day

**Trigger** You fail a Performance check that benefits from the mask's bonus

**Effect** You change the mask's character and reroll the Performance check, using the second result.

**Source:** `= this.source` (`= this.source-type`)
