---
type: deity
source-type: "Remaster"
domains: "Cities, Death, Luck, Sorrow"
favored-weapon: "Dagger"
divine-font: "Harm, Heal"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Jump]], Rank 2: [[Gecko Grip]], Rank 7: [[True Target]]"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In a Sylirican raid on Pol-Reanphoros, the saddle-maker Chinostes took up his tack knife in a desperate attempt to defend his neighbors. His efforts killed the raid's leader and scattered the other warriors, awakening the first spark of his mythic power. Chinostes never abandoned his role as a humble, folk-hero vigilante, even as a hero-god. One day, he tracked and confronted a murderer, only to find this was no mortal foe, but a vampire, who overpowered Chinostes and turned him into one of their kind.

Even so, Chinostes retained his mythic abilities. He still stalks Reanphoros, most often fighting whatever threatens his city-state. However, the occasional citizen vanishes, only to reappear later, drained of blood—a grim price most citizens accept due to the worse evils he keeps at bay.

Two diametrically opposed cults venerate Chinostes. Those calling themselves Nightwardens celebrate his undead majesty and necessary evils. In contrast, the Redeemers keep the older faith, condemning the monster Chinostes has become. To the Redeemers, the greatest service they can ever perform for their hero-god is to drive a stake through his heart. Bizarrely, Chinostes grants spells to both groups, suggesting his tacit approval of both agendas.

**Title** The Fallen Blade

**Areas of Concern** tragedy and sacrifice

**Edicts (Redeemer)** aid your neighbors, wield humble weapons, destroy Chinostes

**Anathema (Redeemer)** hog credit, create undead

**Edicts (Nightwarden)** aid your neighbors, sacrifice others for the greater good, leave cryptic calling cards of your actions

**Anathema (Nightwarden)** disparage others for seeking terrible power to achieve laudable goals

**Religious Symbol** heart pierced by two swords

**Sacred Animal** horse

**Sacred Colors** black and white

**Source:** `= this.source` (`= this.source-type`)
