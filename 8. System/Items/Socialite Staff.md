---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 1900}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *socialite staff* is designed as an ornate cane, its metal body glimmering with jewels and gold inlays. A sculpture carved from obsidian tops the head of the staff, its design depending on its wielder's taste. Common choices include birds, flowers, or family crests. While wielding a socialite staff, you gain a +2 circumstance bonus to [[Make an Impression]] on members of high society.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Read the Air]]
- **1st** [[Charm]], [[Restyle]]
- **2nd** [[Befitting Attire]], [[Phantom Crowd]]
- **3rd** [[Bottomless Stomach]], [[Shift Blame]]
- **4th** [[Befitting Attire]], [[Suggestion]]
- **5th** [[Befitting Attire]], [[Charm]], [[Glimmer of Charm]], [[Suggestion]]

**Craft Requirements** Supply one casting of all listed ranks of all listed spells.

**Source:** `= this.source` (`= this.source-type`)
