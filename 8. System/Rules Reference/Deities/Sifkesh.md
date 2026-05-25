---
type: deity
source-type: "Remaster"
domains: "Nightmares, Pain, Sorrow, Trickery"
favored-weapon: "War-razor"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Ill Omen]], Rank 4: [[Suggestion]], Rank 5: [[Wave Of Despair]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Sifkesh is unusual among demonkind as she is more of a machinator akin to a devil. The Whispered Doubt works on twisting minds away from purity, seducing faithful mortals into betraying their religions. Once tempted into blasphemies, these mortals damage to the reputations of their religion among society and also to their personal standing. Sifkesh particularly delights in pushing these blasphemers to leave their faith, fighting against their fellow faithful, or even leading a mortal to the ultimate ruin of death. In these cases, Sifkesh can more easily claim a heretic's soul and consume it. This consumption borders on the daemonic, which contradicts her demonic nature. Sifkesh appears as a human woman with pale wings, dark hair, and a body cut into sections that float together to maintain her generally humanoid form. Her worshippers include blasphemers, heretics, and outcasts from other religions.

**Title** The Whispered Doubt

**Areas of Concern** Heresy, hopeless despair, suicide

**Edicts** Spread doubt among the faithful, ruin the reputation of religions, provoke wrongdoers to suicide instead of allowing for redemption

**Anathema** Spread hope, offer forgiveness, sincerely honor or call upon another god

**Religious Symbol** bloody hands

**Sacred Animal** asp

**Sacred Colors** red, white

**Source:** `= this.source` (`= this.source-type`)
