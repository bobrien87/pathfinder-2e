---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 4500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A multi-hued array of scales covers a dragonprism staff, forming a gradient of color, and a dragon's claw holds a gem upon the staff's head. Dragons give allies these staves as a mark of esteem. While wielding a dragonprism staff you seem fiercer, gaining a +1 circumstance bonus to Intimidation checks to [[Demoralize]].

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Gouging Claw]], [[Puff of Poison]]
- **1st** [[Breathe Fire]], [[Fear]]
- **2nd** [[Acid Grip]], [[Resist Energy]]
- **3rd** [[Fear]], [[Lightning Bolt]]
- **4th** [[Fly]], [[Reflective Scales]]
- **5th** [[Howling Blizzard]], [[Summon Dragon]]
- **6th** [[Dragon Form]], [[Reflective Scales]], [[Summon Dragon]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
