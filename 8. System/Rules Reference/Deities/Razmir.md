---
type: deity
source-type: "Remaster"
domains: "Magic, Secrecy, Trickery, Wealth"
favored-weapon: "Mace"
divine-font: "Harm"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Charm]], Rank 2: [[Stupefy]], Rank 3: [[Mind Reading]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Razmir, the Living God, was once a mighty wizard who developed a religious regimen known as the 31 Steps. This text dictates how his priests ascend within the hierarchy of his church, and the specific details of these steps can only be learned by first joining his priesthood. Once initiated into Razmir's church, priests are taught the steps in careful and controlled increments; the highest ranking of Razmir's priests are the gold-masked Visions of the 15th Step, and the second-highest rank are the silver-masked Masks of the 12th Step. What the remaining sixteen steps between the Visions and Razmir might be are known only to Razmir and the Visions themselves, though no Vision has yet attained the wisdom and discipline to ascend beyond the 15th Step.

In the days before he brought peace and prosperity to the people of the River Kingdoms, Razmir ascended to godhood in the year 4661 ar, by following the path of the 31 Steps and completing the Test of the Starstone. Following his ascension, Razmir made his way to the Archduchy of Melcat, where his feats of incredible magic power, promises of wealth, and teachings regarding the secret to following in his footsteps caused many to flock to his banner and holy word. Razmir founded his first temple in the Melcatian city of Xer, where he began elevating masked priests to serve him and teaching the doctrine of the 31 Steps. Razmir then annihilated the Duke of Melcat and all his followers for heresy with a potent act of magic, making evidence of his godhood plain for all to see. Razmir's faith and earthly dominion spread quickly through the River Kingdoms after this, though his reign has been plagued by fools who continue the heresies of Duke Melcat. Many others have challenged the might of Razmir and some have even gone so far as to question his divinity, despite the well-recorded evidence of his miracles.

One need only look at the indisputable wealth of Razmiran's people to see the truth of Razmir's divine teachings. One need only hear the fear that trembles in the voices of those who have witnessed the wrath of the Living God and his priests to know that there is no greater god on Golarion.

—A true and indisputable accounting of the glory of Razmir, as recorded in *To Climb the 31 Steps*

**Title** The Living God

**Areas of Concern** law, luxury, obedience

**Edicts** follow the path of the 31 steps, obey those who speak with Razmir's voice, pay tithes and tributes to the Living God

**Anathema** disobey Razmir or one of his priests, question the truth of the Living God

**Religious Symbol** porcelain mask

**Sacred Animal** honeyguide

**Sacred Colors** gold, purple, silver

**Special** A cleric cannot choose Razmir as their deity or gain any of his devotee benefits unless they have the Razmiran priest archetype.

**Source:** `= this.source` (`= this.source-type`)
