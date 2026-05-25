---
type: deity
source-type: "Remaster"
domains: "Air, Cities, Knowledge, Magic"
favored-weapon: "Katar"
divine-font: "Harm"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Charm]], Rank 2: [[Animus Mine]], Rank 3: [[Enthrall]], Rank 4: [[Suggestion]], Rank 5: [[Wave Of Despair]], Rank 6: [[Mislead]], Rank 7: [[Warp Mind]], Rank 8: [[Hidden Mind]], Rank 9: [[Phantasmagoria]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Nyarlathotep is a being of a thousand shapes, each of which has a name, such as the Haunter of the Dark or the Veiled Voice. Because he has walked the world in mortal form, Nyarlathotep is unique among the Outer Gods for appearing comprehensible and understandable—but this is a facade. The Crawling Chaos, as he is also known, appears humanlike not because he identifies with mortal concerns or cares for his mortal followers, but because a mortal shape makes it easier for him to do his work: spreading the influence of the Outer Gods.

**Title** The Faceless Sphinx

**Areas of Concern** Conspiracies, political corruption, vengeance

**Edicts** Indoctrinate the desperate and needy, influence institutions of power to hasten the end of the world

**Anathema** None

**Religious Symbol** featureless face made out of black stone

**Sacred Animal** cat

**Sacred Colors** black, white

**Source:** `= this.source` (`= this.source-type`)
