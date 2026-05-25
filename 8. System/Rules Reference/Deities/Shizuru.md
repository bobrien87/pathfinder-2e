---
type: deity
source-type: "Remaster"
domains: "Duty, Perfection, Sun, Vigil"
favored-weapon: "Katana"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Sure Strike]], Rank 4: [[Reflective Scales]], Rank 7: [[Planar Palace]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Just as the sun defines natural order on earth, Shizuru holds dominion over divine and mundane as the Ruler of Heaven. In some regions she is depicted as a golden dragon surrounded by brilliant light, while more often she is a woman with long, untied hair and armor emblazoned with a rooster. She has been characterized as a committed ruler, an exceptional warrior, a sorrowful lover, and an exacting judge depending on which source one consults. Although sometimes contradictory, Shizuru accepts her myriad representations as long as the foundational principles of order and growth remain unchanged. She feels little need to justify herself or address how her actions are understood. Major centers of followers can be found in Goka, Jinin, Linvarre, Quain, Songbai, Xa Hoi, and Zi Ha, but those seeking to better understand Shizuru inevitably end up in Minkai, for this is the heartland of her worship.

**Title** Ruler of Heaven

**Areas of Concern** ancestors, order, the sun, growth

**Edicts** practice your chosen skill every day, honor your ancestors, protect nature and society from corruption and destruction

**Anathema** abandon a companion in need, harm the innocent, disrespect your ancestors, parlay with truce breakers, separate lovers, cast an unholy spell

**Religious Symbol** katana crossing a sun

**Sacred Animal** carp

**Sacred Colors** red, gold

**Source:** `= this.source` (`= this.source-type`)
