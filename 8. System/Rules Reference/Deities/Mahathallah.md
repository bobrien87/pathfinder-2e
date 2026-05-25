---
type: deity
source-type: "Remaster"
domains: "Fate, Trickery, Truth, Undeath"
favored-weapon: "Bola"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 2: [[Blur]], Rank 5: [[Illusory Scene]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

While the other Queens of the Night are all fallen celestials, Mahathallah was once among the most powerful of the monitors: a psychopomp usher in service of Pharasma. Granted a glimpse of the end of her own existence, Mahathallah fled to the pits of Hell, finding some form of solace in Asmodeus's counsel. Now the Dowager of Illusions, Mahathallah deals in death, fate, and vanity, pulling back the veils of lies that obscure the profound facts of existence. She teaches her followers to seek the truths underlying each falsehood, fomenting arrogance and callousness in them. She also serves as a distant, deliberate advisor to the other Queens of the Night.

**Title** The Dowager of Illusions

**Areas of Concern** Death, fate, vanity

**Edicts** Become an arbiter of reality, capitalize on the ignorance of others, reject conventional wisdom as falsehood

**Anathema** Become too invested in mortal affairs, refuse to hear a truth out of preference for ignorance

**Religious Symbol** bejewled skeletal hand

**Sacred Animal** dragonfly

**Sacred Colors** gold, ivory

**Source:** `= this.source` (`= this.source-type`)
