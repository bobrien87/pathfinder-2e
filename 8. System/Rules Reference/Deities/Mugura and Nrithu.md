---
type: deity
source-type: "Remaster"
domains: "Ambition, Freedom, Passion, Repose"
favored-weapon: "Fist"
divine-font: "Harm"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Shockwave]], Rank 3: [[Hypnotize]], Rank 4: [[Mirror'S Misfortune]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Mugura and Nrithu are a pair of lovers turned rivals, eternally locked in dance, forever testing each other. Theirs is a cautionary tale, one of love and hubris. Mugura was the rambunctious child of a raja and Nrithu was a shy street rat. Their worlds collided due to a passion for dance and both being unable to speak. The two of them quickly grew close, sharing a language of motion and rhythm, exchanging stories of lives worlds apart. Together, they became a beautiful dance duo across Tian Xia, entertaining streets and palaces alike and learning from each corner of the continent. As they grew in talent and fame, so did their devotion to storytelling and each other. Likha, the Teller god, saw this devotion and gave both a boon of godhood to perform together for eternity as well as tell stories to the gods. But then their relationship grew dark. The whims of their followers drew them away from each other and a deep love turned ugly as they bickered over the domains they blessed. With eternity to perform, they each became harsher on the other. Small mistakes compounded as standards grew. Bitter rivalry replaced love as they sabotaged each other in small ways on their cosmic stage, gajjelu ringing out like clashing blades with each step.

**Title** The Divine Dancers

**Areas of Concern** Dance and storytelling, lovers and rivals, fame and gratitude

**Edicts** Practice until perfect, create stories and relationships, trust and listen to your partner

**Anathema** Steal credit from others, upstage or sabotage, spread rumors to get ahead

**Religious Symbol** cloth pieces tied in a wedding knot

**Sacred Animal** gibbon

**Sacred Colors** cream, orange

**Source:** `= this.source` (`= this.source-type`)
