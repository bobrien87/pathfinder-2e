---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Divine]]", "[[Monk]]", "[[Staff]]", "[[Two hand d8]]"]
price: "{'gp': 6500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder #211: The Secret of Deathstalk Tower"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

After she led her people through the Darklands to the far side of the world, the elven oracle Jininsiel established the nation of Jinin in the heart of the continent of Tian Xia. As she sought to forge alliances with other lands surrounding her own, Jininsiel crafted potent magic items as gifts. For the people of Tianjing, she created this staff, which served the people of that nation well for many years. They returned it to Jinin as a token of condolence when that nation's leader passed into the Great Beyond. Many centuries later, when the people of Jinin learned that their kin had returned to Kyonin from Castrovel only to face fiendish threats in their homeland, a group of priests from Jinin traveled across the world to help. They brought with them *Fiendbreaker* and chose to leave it in Kyonin to help protect them in the future from demonic foes.

*Fiendbreaker* functions as a *+2 greater striking holy standard-grade cold iron staff*. While wielding the staff, you gain a +2 circumstance bonus to checks made to [[Recall Knowledge]] about fiends.

**Activate** Cast a Spell

**Effect** You expend a number of charges from the staff to cast a spell from its list.

- **Cantrip** [[Divine Lance]]
- **1st** [[Sanctuary]]
- **2nd** [[See the Unseen]]
- **3rd** [[Anointed Ground]], [[Holy Light]]
- **4th** [[Clear Mind]], [[Planar Tether]]
- **5th** [[Banishment]], [[Divine Wrath]]
- **6th** [[Holy Light]], [[Spirit Blast]]

**Source:** `= this.source` (`= this.source-type`)
