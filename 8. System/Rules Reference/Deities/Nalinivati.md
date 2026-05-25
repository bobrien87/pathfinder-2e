---
type: deity
source-type: "Remaster"
domains: "Magic, Passion, Wyrmkin, Naga"
favored-weapon: "Jaws, Urumi"
divine-font: "Harm, Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Charm]], Rank 2: [[Invisibility]], Rank 3: [[Lightning Bolt]], Rank 4: [[Reflective Scales]], Rank 5: [[Subconscious Suggestion]], Rank 6: [[Mislead]], Rank 7: [[Contingency]], Rank 8: [[Confusing Colors]], Rank 9: [[Wrathful Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Serpent's Kiss

**Areas of Concern** Family, fertility, snakes, sorcery

**Edicts** Seek out magic and use it, use poison, heal poisons, bear or adopt children, raise snakes

**Anathema** Kill a harmless snake or swan, spurn friends due to jealousy or romantic competition, betray your offspring, separate lovers

**Religious Symbol** Lotus flower wherein a snake lies coiled

**Sacred Animal** snake

**Sacred Colors** blue, green, purple

**Source:** `= this.source` (`= this.source-type`)
