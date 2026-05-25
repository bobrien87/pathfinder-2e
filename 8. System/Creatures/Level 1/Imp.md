---
type: creature
group: ["Fiend", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Imp"
level: "1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Tiny"
trait_01: "Fiend"
trait_02: "Unholy"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Common, Diabolic, Chthonian, Daemonic (Telepathy (Touch))"
skills:
  - name: Skills
    desc: "Acrobatics +7, Arcana +6, Deception +7, Religion +5"
abilityMods: ["-1", "+4", "+0", "+1", "+2", "+2"]
abilities_top:
  - name: "Telepathy (Touch)"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Imp Venom"
    desc: "**Saving Throw** DC 16 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Clumsy]] 1 (1 round) <br>  <br> **Stage 2** 1d6 poison damage, clumsy 1, and [[Slowed]] 1 (1 round)"
armorclass:
  - name: AC
    desc: "17; **Fort** +5, **Ref** +9, **Will** +7"
health:
  - name: HP
    desc: "15; **Weaknesses** holy 3; **Resistances** poison 3"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Stinger +9 (`pf2:1`) (agile, finesse, magical, reach 0 ft., unholy), **Damage** 1d4-1 piercing plus [[Imp Venom]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 17, attack +9<br>**4th** [[Read Omens]]<br>**2nd** [[Invisibility (At Will, Self Only)]]<br>**1st** [[Charm]], [[Detect Magic]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The imp takes on the appearance of a Medium or smaller animal. While transformed, the imp loses their normal senses, innate spells, and special actions, but doesn't otherwise change their statistics and can still speak and use telepathy. The imp also gains any special senses of the animal and any Speeds the animal has. <br>  <br> This doesn't change the attack and damage modifiers of their Strikes but might change the damage type their Strikes deal (depending on what kinds of attacks the animal has) and prevents them from exposing creatures to imp venom. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Fiendish Healing"
    desc: "`pf2:1` **Frequency** once per round. <br>  <br> **Effect** The imp regains 1d6 healing Hit Points."
  - name: "Fiendish Temptation"
    desc: "`pf2:1` **Frequency** once per day <br>  <br> **Effect** The imp offers a nonfiend within 15 feet a bargain, granting a boon of good luck if the creature accepts voluntarily. The boon lasts for 1 hour once accepted. <br>  <br> Once during the hour, the creature can roll an attack roll or saving throw twice and use the higher result. If the creature dies while the boon is in place, the imp decides where the creature's soul travels. This typically makes the soul bound for eternity in the imp's home plane, and the creature unable to be raised or resurrected except by the [[Wish]] ritual or similar magic."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Imps are fiendish infiltrators and corrupters who, despite their diminutive stature, are more than capable of subtly influencing a weak-willed individual into performing increasingly evil acts over time. An imp will often agree to serve a mortal and act docile and loyal in a long-term plot to eventually get their master killed or damn their soul. Imps are born directly from the Outer Planes themselves, rather than from mortal souls, and thus they serve outside any fiendish hierarchies, granting them leeway to pursue their specialties. Despite standing a mere 2 feet tall, imps can be vicious combatants, flying out of reach and turning invisible to escape should the odds turn against them.

```statblock
creature: "Imp"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
