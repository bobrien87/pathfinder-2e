---
type: creature
group: ["Demon", "Fiend"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pusk"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Demon"
trait_02: "Fiend"
trait_03: "Unholy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Darkvision]]"
languages: "Chthonian (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +8, Deception +6, Stealth +6"
abilityMods: ["+4", "+0", "+4", "-3", "+0", "+0"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Sloth"
    desc: "When a pusk regains their actions, roll 1d4. The pusk regains that many actions for the turn (to a maximum of 3, or 2 if the pusk is a minion). <br>  <br> Effects like the slowed condition can further reduce their number of actions."
  - name: "Vicious Criticals"
    desc: "A pusk makes the most of any weakness it finds. Whenever a pusk scores a critical hit with its claw Strike, the target takes an additional 1d6 persistent bleed damage."
armorclass:
  - name: AC
    desc: "17; **Fort** +10, **Ref** +4, **Will** +8"
health:
  - name: HP
    desc: "36; **Weaknesses** cold iron 3, holy 3"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +10 (`pf2:1`) (magical, unarmed, unholy), **Damage** 1d8+4 piercing"
  - name: "Melee strike"
    desc: "Claw +10 (`pf2:1`) (agile, magical, unarmed, unholy), **Damage** 1d6+4 slashing"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 16, attack +8<br>**3rd** [[Slow]]<br>**1st** [[Fear]]"
abilities_bot:
  - name: "Cower"
    desc: "`pf2:1` The pusk makes itself as small as possible, protecting its vital organs with its limbs. It gains a +4 circumstance bonus to AC but takes a –2 penalty to attack rolls. This lasts until the pusk moves from its current space, falls [[Unconscious]], or ends the effect as a free action."
  - name: "Frenzied Slashes"
    desc: "`pf2:3` The pusk makes three claw Strikes, each at a –2 penalty, all targeting the same creature. The pusk's multiple attack penalty doesn't increase until after it has made all three attacks. The pusk gains the [[Clumsy]] 2 condition until the beginning of its next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Among the lowest and least powerful of all demons, the wretched pusks are just as vicious and cruel as their more powerful brethren. They happily vent their frustrations on anything weaker than themselves.

Born from the souls of the slothful, these demons appear vaguely humanoid in appearance with awkward limbs and slack lumps of skin hanging from their frames. Supposedly, a single slothful soul of sufficient depravity and strength can spawn an entire horde of these creatures. However, as weaker demons, their lot in life is to suffer at the hands of more powerful Abyssal predators, and only a tiny number of pusks ever manage to become something more. For this reason, pusks are quite accommodating when summoned by mortals. They're usually content to work under conditions few other fiends would accept, although they'll still gladly turn on even the kindest of masters who show even the slightest hint of weakness.

When a sinful mortal soul is judged and sent on to the Outer Rifts, it can become a deadly fiend—a demon. Demons are living incarnations of sin—be they classic sins like wrath or gluttony, or more "specialized" depravities like an obsession with torture or the act of treason or treachery. Once formed, a demon's driving goals are twofold—the amassing of personal power, and the corruption of mortal souls to cause them to become tainted by sin. In this way demons ensure a never-ending supply of new demons to bolster their ever-growing ranks in the Outer Rifts.

Demons are selfish and self-absorbed creatures, and most firmly believe that mortals only play at being more virtuous than fiends. They enjoy tempting mortals into damnation to both indulge their egos and swell their armies. Like many other fiends, one of the great rewards of this manipulation is fulfilling their hunger for souls. In their eyes, the primary use for these souls is to spawn new demons, who can serve as soldiers, slaves, pawns, or even currency for their more powerful masters.

```statblock
creature: "Pusk"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
