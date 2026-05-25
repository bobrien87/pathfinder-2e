---
type: deity
source-type: "Remaster"
domains: "Air, Nature, Travel, Water"
favored-weapon: "Trident"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Gust Of Wind]], Rank 3: [[Lightning Bolt]], Rank 5: [[Control Water]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

When the wind first rippled the waves of the primordial ocean, Gozreh was born. This timeless, inscrutable entity is a being of dualities: wind and wave, male and female, generous and ravenous, benevolent and disastrous. Mortal kind has marveled at Gozreh from the beginning, as they've been lashed by storms, paying visceral witness to the Wind and the Waves in a manner more immediate than the abstract reality of most gods. Then and now, worshippers reverently slip offerings overboard or burn incense that wafts aloft, hoping to please Gozreh but content to avoid the god's displeasure. Even followers who successfully placate the tempestuous god know better than to trust their favor for long, as Gozreh's pleasure waxes and wanes like the tide, and their forbearance passes swiftly as a gust. Gozreh's pique is just as temporary. Storms pass, and the sea calms. With the god's attention on all the world's waters and winds, Gozreh's fury is unlikely to linger in one place for long.

**Title** The Wind and the Waves

**Areas of Concern** nature, the sea, weather

**Edicts** cherish, protect, respect nature in all its forms

**Anathema** bring civilization to intrude on the wild, create undead, despoil areas of natural beauty

**Religious Symbol** dripping leaf

**Sacred Animal** all

**Sacred Colors** blue, green

**Source:** `= this.source` (`= this.source-type`)
