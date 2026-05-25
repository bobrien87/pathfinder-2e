---
type: deity
source-type: "Remaster"
domains: "Cities, Duty, Freedom, Protection"
favored-weapon: "Tekko-kagi"
divine-font: "Heal"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Protector Tree]], Rank 2: [[Oaken Resilience]], Rank 4: [[Wall Of Fire]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In life, Uirch was a follower of Sarenrae and a warpriest in the Burning Sun hold under warlord Mahja. He became a god upon usurping the tyrannical god Lanishra. Like Mahja, Uirch has incorporated much of Sarenrae's teachings into his own, but his primary goals are to protect those who cannot protect themselves and prevent tyranny from taking root. Prior to his ascension, Uirch spent much of his time learning various ways to protect people, both physically and mentally. He also studied the most impactful preventive measures to ensure people wouldn't need protection in the first place. One such measure that Uirch strongly advocates is inhibiting tyranny from taking hold. He encourages leaders to be strong and benevolent, but also to ensure that there exists a system to keep a watchful eye out for those in power who might exceed the duties of their station and become tyrants. He instructs all his followers to do the same, and there are already several small orc holds adopting his philosophies and placing his priests in positions as guides and counselors.

**Title** The Bulwark

**Areas of Concern** Fortifications, leadership, protection

**Edicts** Protect the weak and innocent, keep your word, do not throw your life away needlessly

**Anathema** Allow tyranny to stand uncontested, put your own safety before those in need of defending, make a promise with the intent to break it

**Religious Symbol** blazing sun on a shield

**Sacred Animal** brown bear

**Sacred Colors** green, brown

**Source:** `= this.source` (`= this.source-type`)
