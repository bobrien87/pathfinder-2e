---
type: deity
source-type: "Remaster"
domains: "Change, Freedom, Introspection, Might"
favored-weapon: "Ranseur"
divine-font: "Harm, Heal"
divine-skill: "Athletics"
divine-spells: "Rank 1: [[Grim Tendrils]], Rank 5: [[Illusory Scene]], Rank 6: [[Vibrant Pattern]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Neshen, Knight of the Steel Lash, is a loving but harsh god, demanding that those who come to him show they have truly changed through the trials he gives them. More hands on with the fate of his followers than many other gods, Neshen is known to manipulate situations to ensure that those who have turned to him really do plan to turn away from their previous lives. This can be as simple presenting them a temptation of the flesh, placing them on the receiving end of a fight, or even having them imprisoned for that which they have done before. Neshen doesn't believe that change should be easy, but meaningful. Through meaningful change, his worshippers are those who tread closest to the light.

**Title** Knight of the Steel Lash

**Areas of Concern** Knight of the Steel Lash

**Edicts** Lead others to the light of good, strive for self-perfection, be a support for others struggling to change their ways

**Anathema** Stop taking care of yourself, wallow in self-pity, refuse to right past wrongs

**Religious Symbol** coiled steel lash

**Sacred Animal** ram

**Sacred Colors** iron gray, red

**Source:** `= this.source` (`= this.source-type`)
