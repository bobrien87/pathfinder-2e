---
type: item
source-type: "Remaster"
level: "21"
traits: ["[[Artifact]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "worn"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

At the center of this silver ring gleams an obsidian gem, its surface emblazoned with a bloodred rune of forgetting. While wearing a *forgotten signet*, you're subjected to [[Hidden Mind]] (+32 counteract bonus) and easily fade from others' memory. Sapient creatures must attempt a DC 42 [[Will]] save each time you depart from their company or they forget you entirely.
- **Critical Success** The creature's memories of you are normal.
- **Success** The creature remembers you and your interactions but has difficulty describing either to others. Each time they attempt to share information about these subjects with someone else, they relate only confusing or unclear details about you and this interaction.
- **Failure** The creature remembers your existence but no details about you or your interactions. For example, they remember speaking with an individual of your most basic biological traits, such as a human woman, but not your name, appearance, or other specific features.
- **Critical Failure** The creature retains no memories of you or this interaction.

**Destruction** If a creature learns the true name of a *forgotten signet*'s wearer and makes it public knowledge, that *forgotten signet* tarnishes and breaks in two.

**Source:** `= this.source` (`= this.source-type`)
