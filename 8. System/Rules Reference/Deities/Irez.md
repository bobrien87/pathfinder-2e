---
type: deity
source-type: "Remaster"
domains: "Fate, Glyph, Luck, Magic"
favored-weapon: "Dart"
divine-font: "Heal"
divine-skill: "Arcana"
divine-spells: "Rank 1: [[Anticipate Peril]], Rank 2: [[Umbral Extraction]], Rank 4: [[Reflective Scales]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Cards, glyphs, scribes, and spells are all the purview of the Lady of Inscribed Wonder. She holds knowledge and understanding of the great power and symbolism behind runes. In particular, Irez understands how runes can supplement and empower arcane magic. It's through this understanding that Irez is able to make enigmatic predictions on events in the distant future, which more often than not come to pass. Many of her followers are calligraphers, gamblers, harrow readers and others who regularly handle cards and symbols, be they for an arcane purpose, prophetic practices, or their more mundane applications.

**Title** Lady of Inscribed Wonder

**Areas of Concern** Cards, scribes, spells

**Edicts** Read fortunes, practice calligraphy, devise and study runes

**Anathema** Destroy magic scrolls, cheat at games of chance, deliberately write illegibly

**Religious Symbol** fan of parchment strips

**Sacred Animal** roc

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
