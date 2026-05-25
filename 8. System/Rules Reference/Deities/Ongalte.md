---
type: deity
source-type: "Remaster"
domains: "Ambition, Destruction, Fate, Void"
favored-weapon: "Greataxe"
divine-font: "Harm"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Sure Strike]], Rank 2: [[Paranoia]], Rank 6: [[Disintegrate]]"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

When cyclopes and Iblydans first joined forces, they lived as equals. However, humanity gradually overshadowed their giant colleagues, with cyclopes uplifting hero-gods but rarely becoming divine themselves. As she trained in the art of myth-speaking, the cyclops Ongalte became bitter at her species' decline and humans' ascendancy. Without change, her people would eventually dwindle and vanish entirely. She enacted her own myth-speaking, soon after which she collapsed the temple, crushing her and many others beneath the rubble. Yet moments later, she emerged unscathed and ascendant.

Since then, Ongalte has haunted Iblydos as a hero-god of deicide. She has killed at least three hero-gods, and she may have orchestrated others' demises without formally claiming responsibility. Her greatest obstacles are the city-states themselves; surviving hero-gods rarely leave their urban sanctuaries, so Ongalte relies on slander and disgrace to force these demigods into the open.

Ongalte has only elevated one hero-god other than herself: her lieutenant Ytildos. His betrayal decades ago confirmed her belief that all hero-gods must die.

**Title** The Death of Divinity

**Areas of Concern** deicide

**Edicts** ruin the reputation of other hero-gods, aid those whom the hero-gods have wronged, kill gods

**Anathema** make a sincere prayer to any other hero-god, perform deeds that ultimately glorify another hero-god

**Religious Symbol** pierced skull of a cyclops

**Sacred Animal** parasitic wasp

**Sacred Colors** gray, red

**Source:** `= this.source` (`= this.source-type`)
