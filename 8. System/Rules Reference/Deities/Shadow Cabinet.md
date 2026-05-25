---
type: deity
source-type: "Remaster"
domains: "Ambition, Darkness, Secrecy, Trickery"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 4: [[Clairvoyance]], Rank 6: [[Mislead]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Though they would never admit to it, followers of the Shadow Cabinet venerate the ideas of secrecy and control. They are often power brokers working behind the scenes to pull the strings of governmental leaders or spies, and double agents uncovering information for their own twisted schemes. Adherents of this covenant have been known to work together for a common goal and usually go their separate ways before any individual plans cause conflict. After all, these faithful are usually more plotters and planners than they are fighters. Though, of course, a well-timed secret dagger in the heart or lethal dose of poison can sometimes more quickly further an agenda than months of whispers and subtle machinations. The Shadow Cabinet's benefactors include deities of secrets and opportunities like the Vudrani goddess Dhalavei and the halfling god Thamir, as well as powerful shadow beings. Many are convinced that this covenant could not thrive or even hope to exist without Norgorber's tacit approval, but the Gray Master and his priests have neither confirmed nor denied his involvement.

**Covenant Members** Dhalavei, Norgorber (rumored), Thamir, powerful shadows

**Areas of Concern** opportunities, secret agendas and alliances, shadow governments, spies

**Edicts** glean sensitive information through underhanded means, infiltrate powerful organizations, keep your own secrets

**Anathema** allow your agenda to be discovered through carelessness, destroy information when it doesn't personally benefit you

**Religious Symbol** dagger dripping ink

**Source:** `= this.source` (`= this.source-type`)
