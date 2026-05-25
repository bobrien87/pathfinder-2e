---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Pukwudgie"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Low-Light Vision]]"
languages: "Common, Elven, Fey, Gnomish"
skills:
  - name: Skills
    desc: "Crafting +15, Deception +14, Medicine +15, Nature +17, Stealth +17, Thievery +15"
abilityMods: ["+4", "+6", "+3", "+4", "+6", "+3"]
abilities_top:
  - name: "Pukwudgie Poison"
    desc: "**Saving Throw** DC 25 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Stupefied 1]] (1 round) <br>  <br> **Stage 2** 1d6 poison damage and [[Stupefied 2]] (1 round) <br>  <br> **Stage 3** 1d6 poison damage, [[Confused]], and stupefied 2 (1 round)"
armorclass:
  - name: AC
    desc: "25; **Fort** +12, **Ref** +15, **Will** +17"
health:
  - name: HP
    desc: "100; **Weaknesses** cold iron 10; **Resistances** poison 5"
abilities_mid:
  - name: "Defensive Quills"
    desc: "A creature that hits a pukwudgie with an unarmed Strike or a non-reach melee Strike takes 3d8 piercing damage (DC 22 [[Reflex]] save). On a critical failure, the creature also takes 1d6 persistent,poison from the poisoned quills. <br>  <br> *Note: A DC was not provided for this ability by Paizo. The DC present here is a moderate DC for the creature level according to the GM Core creature building Tables*"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hatchet +17 (`pf2:1`) (agile, magical, sweep), **Damage** 1d6+10 slashing plus [[Pukwudgie Poison]]"
  - name: "Melee strike"
    desc: "Hatchet +19 (`pf2:1`) (magical, thrown 10), **Damage** 1d6+10 slashing plus [[Pukwudgie Poison]]"
  - name: "Ranged strike"
    desc: "Shortbow +18 (`pf2:1`) (deadly d10, range 60 ft.), **Damage** 1d6+6 piercing plus [[Pukwudgie Poison]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 25, attack +17<br>**4th** [[Mirage]], [[Unfettered Movement]]<br>**3rd** [[Wall of Thorns]]<br>**2nd** [[Invisibility (At Will) (Self Only)]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The pukwudgie takes on the physical form of a giant porcupine or resumes their natural form. In porcupine form, their size changes to Medium, they lose their weapon Strikes, and they gain a quill Strike (+18 for 2d8+6 piercing plus 1d8 persistent poison). <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Pukwudgies go by many names in many regions, but those who know of them agree that defying their mischievous nature provokes their wrath.

In ancient times, pukwudgies traveled to the Universe from the First World, perhaps in the wake of the gnome emigration. These proud fey are obsessed with displays of respect, and while they first attempted to befriend mortals, each attempt ended in tragedy as the pukwudgies perceived any potential slight as a grave insult. Mortals, fearing these reactions, began to view pukwudgies as dangerous nuisances. Pukwudgies, in turn, began to resent mortals and the gods that favored them.

At their best, pukwudgies play cruel jokes on mortals they encounter. At their worst, they've been known to kidnap and even kill those who don't treat them with proper respect. Violent fey like twigjacks and redcaps often gather under pukwudgie leadership, much to the pukwudgies' glee.

Pukwudgies make their villages in the oldest forests, concealed under [[Mirage]] spells. They travel freely between the Universe and the First World through tiny portals beneath hills, trees, or stones. No strangers to violence, pukwudgies rarely travel alone and often anoint their quills or weapons with a custom-brewed poison before entering hostile situations.

Standing about 2 feet tall, a pukwudgie sports sharp quills growing from their head that extends down their back. Their skin tone varies by the region in which they live, ranging from pale gray to brown.

```statblock
creature: "Pukwudgie"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
