---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Divine]]", "[[Magical]]"]
price: "{'cp': 0, 'gp': 160, 'pp': 0, 'sp': 0}"
usage: "etched-onto-clan-dagger"
bulk: "L"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This filigree grants you, as the clan dagger's owner, a +1 item bonus to Society checks and to Diplomacy checks to Request. Additionally, once per day, the filigree symbol can be activated to compel an enemy to act.

**Activate—Vow Unbreakable** `pf2:1` (auditory, concentrate, linguistic, mental)

**Frequency** once per day

**Effect** You command a creature within 30 feet to Stride away from you, drop [[Prone]], or release one item it's holding. The creature can choose to perform that action as the first action on its next turn; if it doesn't, it takes @Damage[4d6[mental]|traits:auditory,concentrate,linguistic,mental] damage (DC 20 [[Will]] save).

**Source:** `= this.source` (`= this.source-type`)
