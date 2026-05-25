---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Cursed]]", "[[Intelligent]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +9; precise vision 30 feet, imprecise hearing 30 feet

**Communication** telepathy (two common languages)

**Skills** Intimidation +9, one skill associated with their use +9

**Int** +2, **Wis** +2, **Cha** +2

**Will** +7

Tools that are severely misused or left in malevolent circumstances can develop malicious sapience, dedicated to critiquing those who use them. Such heckling tools are often born from implements useful to adventurers because such people are the likely to misuse tools or leave them in a corrupting situation. When you first set to using the tools, they fuse to you. Used for their intended purpose, the tools telepathically badger and disparage you, mocking your abilities and giving you ill-founded advice. You must succeed at a DC 19 [[Will]] save to realize this badgering comes from the tools and not your own negative thoughts. Instead of the tool's usual bonus, you take a –2 circumstance penalty to checks made using heckling tools. Once you realize the tools are cursed, you can suppress their negative effects, gaining their typical bonus for 24 hours if you succeed at a DC 17 [[Deception]] check or DC 17 [[Diplomacy]] check to placate them, often by offering obsequious, public admiration.

**Source:** `= this.source` (`= this.source-type`)
