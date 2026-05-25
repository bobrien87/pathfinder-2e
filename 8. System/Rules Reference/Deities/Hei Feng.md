---
type: deity
source-type: "Remaster"
domains: "Air, Indulgence, Lightning, Water"
favored-weapon: "Jiu-huan-dao"
divine-font: "Harm, Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Gust Of Wind]], Rank 4: [[Hydraulic Torrent]], Rank 6: [[Chain Lightning]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Hei Feng, the tengu god of storms, is as unpredictable as the sea, as destructive as a hurricane, and, more often than not, as drunk and foulmouthed as the sailors who pray to him. Impulsive and passionate, his heart moves between joy, sorrow, and anger in the time it takes him to finish his cup, though whatever his mood, he rarely feels it lightly. He may be so moved by a fisher's prayer that he blesses her with a catch large enough to feed her village, while later unleashing torrential waves against that same village for a slight. This unpredictability leads the rest of the Heavenly Court to regard him as troublesome, and mortals to view him with wary respect.

**Title** Duke of Thunder

**Areas of Concern** sailors, the sea, storms, tengu

**Edicts** follow your passion, make token attempts to apologize to those you have wronged, respect the power of the sea and sky, encourage flashy entertainment

**Anathema** fake friendship with those you despise; disrespect Hei Feng or Hei Feng's estranged wife Lady Jingxi; ignore an affront to you, Hei Feng, or Lady Jingxi

**Religious Symbol** lightning bolt issuing from a dark storm cloud

**Sacred Animal** raven

**Sacred Color** black, yellow

**Source:** `= this.source` (`= this.source-type`)
