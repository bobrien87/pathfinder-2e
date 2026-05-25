---
type: deity
source-type: "Remaster"
domains: "Knowledge, Magic, Secrecy, Travel"
favored-weapon: "Gauntlet"
divine-font: "Harm, Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Vanishing Tracks]], Rank 2: [[Invisibility]], Rank 4: [[Flicker]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Rumors say that to glance upon the hooded face of Ng is to either see truth or face oblivion itself, but the Eldest of changing seasons, secrets, and wanderers keeps his visage perpetually shrouded. He is a serious and stern figure draped in silvery robes that swish around his legs as he walks lonely and distant paths. No carefree wanderer, Ng is a patron of those who travel long distances with purpose, and he sometimes shields them from banditry, treacherous weather, and getting lost. Ng keeps many secrets, even from his followers, and none know what his evidently aimless travels might portend. Ng rules over the seasons as they turn one into another, but he rules far more numerous seasons than the four familiar to Golarion, such as the Season of Carnivorous Light and the Season of Solemn Deliquescence.

**Title** The Hooded

**Areas of Concern** The Seasons, secrets, wanderers

**Edicts** Travel, hide your identity and your motives

**Anathema** Sleep in the same place twice in a row, wear seasonal decorations out of season

**Religious Symbol** silver hood containing stars

**Sacred Animal** migratory animals

**Sacred Colors** silver

**Source:** `= this.source` (`= this.source-type`)
