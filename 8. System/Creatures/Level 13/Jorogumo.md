---
type: creature
group: ["Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Jorogumo"
level: "13"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+26; [[Darkvision]]"
languages: "Aklo, Common (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +25, Athletics +23, Crafting +22, Deception +28, Diplomacy +26, Performance +24, Stealth +23, Survival +24"
abilityMods: ["+6", "+4", "+5", "+3", "+5", "+7"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Jorogumo Venom"
    desc: "**Saving Throw** DC 32 [[Fortitude]] save <br>  <br> **Maximum Duration** 4 hours <br>  <br> **Stage 1** 3d6 poison damage and [[Stupefied 1]] (1 round) <br>  <br> **Stage 2** 3d6 poison damage and [[Stupefied 2]] (1 round) <br>  <br> **Stage 3** 4d6 poison damage and stupefied 2 (1 round) <br>  <br> **Stage 4** [[Paralyzed]] for 1d4 hours"
  - name: "Web Trap"
    desc: "A creature hit by the jorogumo's web attack is [[Immobilized]] and stuck to the nearest surface, preventing the creature from moving. The DC to [[Escape]] or [[Force Open]] the web trap is 32."
armorclass:
  - name: AC
    desc: "33; **Fort** +22, **Ref** +23, **Will** +26"
health:
  - name: HP
    desc: "270; **Weaknesses** peachwood 10; **Resistances** poison 15"
abilities_mid:
  - name: "Darting Legs"
    desc: "`pf2:r` **Requirements** The jorogumo has their spider legs extended or has Changed Shape <br>  <br> **Trigger** The jorogumo is targeted with an attack <br>  <br> **Effect** The jorogumo raises a leg, gaining a +2 circumstance bonus to AC against the triggering attack."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +27 (`pf2:1`), **Damage** 3d12+14 piercing plus [[Jorogumo Venom]]"
  - name: "Melee strike"
    desc: "Claw +27 (`pf2:1`) (agile), **Damage** 3d8+14 slashing"
  - name: "Ranged strike"
    desc: "Web +23 (`pf2:1`) (range 60 ft.), **Damage**  plus [[Web Trap]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 34, attack +26<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Outcast's Curse]], [[Suggestion]]<br>**3rd** [[Mind Reading]] (At Will)<br>**2nd** [[Speak with Animals]] (Constant)<br>**1st** [[Charm]] (At Will), [[Summon Animal (Spiders Only)]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The jorogumo takes on the appearance of any Small or Medium spider. This doesn't change their Speed or Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Spider Legs"
    desc: "`pf2:1` **Requirements** The jorogumo is in humanoid form <br>  <br> **Effect** Eight large spider legs sprout from the jorogumo's back, granting a 40-foot climb Speed and allowing them to use the Darting Legs reaction."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Appearing as beautiful, well-dressed humans, jorogumo lurk in the high mountains and prey on travelers, often through words and charm. These cruel creatures can fully change into a giant spider or sprout spider legs from their backs, and they often keep giant spiders as pets. Jorogumo usually eat their prey, but some humanoids meet an even more gruesome fate as living incubators for jorogumo eggs.

When they encounter a tengu, jorogumo fly into a rage and attempt to murder them as quickly as possible, for they insist that tengu can see through their trickery with a mere glance and are immune to their venom, but it isn't clear to outsiders if this is the whole story behind their single-minded hatred. Though most jorogumo are solitary creatures, some worship Norgorber and serve as valuable allies to thieves' guilds following that god's guise as the Gray Master.

```statblock
creature: "Jorogumo"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
