---
type: deity
source-type: "Remaster"
domains: "Confidence, Destruction, Might, Zeal"
favored-weapon: "Longbow, Shortbow"
divine-font: "Harm"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Sure Strike]], Rank 3: [[Wall Of Wind]], Rank 4: [[Weapon Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

General Susumu, also known as the Black Daimyo, is the Tian Xia patron deity of samurai who are interested more in glory and battle than honor and heroism. He is the brother of Shizuru, and the two seldom see eye to eye. His unholy symbol is a black winged horse, and he is worshiped primarily in Chu Ye, Hongal, Kaoling, Minkai, Shokuro, and Xa Hoi.

**Title** The Black Daimyo

**Areas of Concern** Fear, glory, warfare, death

**Edicts** Seek glory in battle, loudly proclaim your victories, protect your possessions and strongholds

**Anathema** Cower from fights, refuse a challenge from an equal, mistreat your weapons, abuse your mount

**Religious Symbol** black winged horse

**Sacred Animal** horse

**Sacred Colors** black, blue

**Source:** `= this.source` (`= this.source-type`)
