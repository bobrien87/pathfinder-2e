---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Elf]]", "[[Finesse]]", "[[Forceful]]", "[[Magical]]"]
price: "{'gp': 6500}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder #211: The Secret of Deathstalk Tower"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking astral elven curve blade* was the treasured weapon of the Calistrian witch Silisifex, who played several key roles in reclaiming Kyonin from Tanglebriar when the elves returned to Golarion. Although a witch, her mesmerizing skill with the curved blade rivaled that of many soldiers. Her reasons for leaving *Soulcutter* behind in Kyonin before her final mission into Tanglebriar in an attempt to purify Deathstalk Tower are unknown.

As long as you carry *Soulcutter*, you gain its potency bonus as an item bonus to all saving throws against mental effects. This bonus increases by 2 against possession effects.

**Activate—Soothe Souls** `pf2:2` (concentrate, healing, manipulate, primal, vitality)

**Frequency** once per day

**Effect** You whirl *Soulcutter* in the air around you, rejuvenating the living within a @Template[type:emanation|distance:20] around you while castigating those in that area who have no place in nature. You can Sustain this activation for up to 1 minute. Living creatures that start their turn in the area regain 1d8 Hit Points, and any fiend or undead creature that starts its turn in the area takes 1d8 spirit damage.

**Activate—Soulcutting Storm** `pf2:2` (concentrate, manipulate, primal)

**Frequency** once per day

**Effect** You swing *Soulcutter* and cast a 7th-rank [[Weapon Storm]] to your specifications, but all damage caused by the spell is spirit damage. If used to damage a creature that's possessing another creature, this spell does no damage to the possessed creature.

**Source:** `= this.source` (`= this.source-type`)
