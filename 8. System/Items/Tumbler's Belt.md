---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 3000}"
usage: "wornbelt"
bulk: "L"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This sparkling purple belt was made for the youngest member of a family of jugglers and tumblers who traveled with the Crascondo Company. The thought was this would allow the child to safely participate with their elder siblings and cousins, but the belt found itself being "loaned" more and more often to dare-taking elders in the troupe. The *tumbler's belt* grants a +2 item bonus to Acrobatics checks, and whenever you critically succeed at a check to [[Tumble Through]], you gain a +10-foot item bonus to your Speed until the end of your turn. While wearing the *tumbler's belt*, you're not [[Off Guard]] while you [[Balance]].

**Activate—Land With Grace** `pf2:r`

**Frequency** once per day

**Trigger** You're falling

**Effect** Treat your fall as if it were 120 feet shorter. Regardless of whether you take damage or not from the fall, you land on your feet.

**Source:** `= this.source` (`= this.source-type`)
