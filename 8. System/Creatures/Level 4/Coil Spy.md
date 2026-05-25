---
type: creature
group: ["Humanoid", "Serpentfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Coil Spy"
level: "4"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Serpentfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+10; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Aklo, Common, Dwarven, Gnomish, Sakvroth (Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +10, Deception +13, Diplomacy +11, Intimidation +11, Occultism +10, Society +10, Stealth +12, Thievery +12"
abilityMods: ["+2", "+4", "+1", "+4", "+2", "+5"]
abilities_top:
  - name: "Maintain Disguise"
    desc: "A Coil spy can maintain an ongoing [[Illusory Disguise]] as long as they are conscious without having to re-cast the spell; they need only Cast the Spell again to reassume their *illusory disguise* if they wish to change their appearance or if the active spell is dispelled. <br>  <br> Coil spies typically seek privacy when they need to sleep, as an ongoing *illusory disguise* ends an hour after they fall [[Unconscious]]."
  - name: "Serpentfolk Venom"
    desc: "**Saving Throw** DC 19 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d4 poison damage and [[Enfeebled]] 1 (1 round) <br>  <br> **Stage 2** 2d4 poison damage and enfeebled 1 (1 round)"
  - name: "Sneak Attack"
    desc: "The Coil spy's Strikes deal an extra 2d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "22; **Fort** +9, **Ref** +12, **Will** +10 ; +1 status to all saves vs. magic"
health:
  - name: HP
    desc: "48; **Resistances** poison 5"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "+4 Status to Will Saves vs. Mental"
    desc: ""
  - name: "Thin of Blood"
    desc: "Coil spies recover slowly from injuries. When they take physical damage from a critical hit, they gain 1d4 persistent,bleed damage. They take a –2 circumstance penalty to flat checks to recover from persistent damage and saving throws against afflictions."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shortsword +14 (`pf2:1`) (agile, finesse, versatile s), **Damage** 1d6+5 piercing plus [[Serpentfolk Venom]]"
  - name: "Melee strike"
    desc: "Fangs +14 (`pf2:1`) (finesse), **Damage** 1d6+5 piercing plus [[Serpentfolk Venom]]"
  - name: "Ranged strike"
    desc: "Hand Crossbow (Spider Venom) +10 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+3 piercing plus [[Spider Venom]]"
  - name: "Ranged strike"
    desc: "Hand Crossbow (Serpentfolk Venom) +10 (`pf2:1`) (reload 1, range 60 ft.), **Damage** 1d6+3 piercing plus [[Serpentfolk Venom]]"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 21, attack +13<br>**4th** [[Suggestion]]<br>**2nd** [[Blur (Self Only, At Will)]]<br>**1st** [[Illusory Disguise]] (At Will), [[Ventriloquism]] (At Will)"
abilities_bot:
  - name: "Deceptive Reposition"
    desc: "`pf2:1` The Coil spy Strides up to half their Speed and attempts a [[Feint]], in either order."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Some serpentfolk undergo intense ritual training and practice to improve their innate ability to disguise themselves. These serpentfolk often identify as members of a sinister society known as the Coils of Ydersius, and the most devoted of their number seek out methods of reincarnating into new forms to infiltrate enemy societies even more efficiently. Coil spies train in methods of infiltrating other societies to such an extent that they might be capable of infiltrating a mammalian civilization for years. Though they're expected to work entirely toward the eventual triumph of their people, most Coil spies also find personal pursuits. When Coil spies get caught, it's rarely due to a lack of skill, but rather to their arrogance or recklessness as they pursue their hedonistic desires.

Before their ancient clash with humanity devastated their civilization, serpentfolk were masters of a sprawling underground empire. Their power was shattered and their god Ydersius decapitated (although not quite slain). The cunning, intelligence, and magical abilities of serpentfolk have diminished from their ancient heights, and most are born without these boons. This is partially the result of cruel genetic meddling among serpentfolk—though the ruling class, zyss, are born with an innate spellcasting ability, their blood runs thin, making them susceptible to wounds. Seen as the failures of the serpentfolk's experiments are the aapophs, who are strong but prone to mutation and lack innate spellcasting.

Today, the central realm of the Darklands retains the old name of the serpentfolk empire that once dominated this region—Sekamina. This name is also the source of the serpentfolk's Aklo title, sekmin, which they are often called in ancient texts. Serpentfolk dominion had declined before ghouls, gugs, umbral gnomes, and other forces. Yet their recent ventures have brought them back to a stronger place in the Darklands. Many serpentfolk sleeping in torpor in secluded vaults have awakened.

Zyss serpentfolk tend toward megalomania, with dreams of returning to their place of dominance. Many of their plans hinge on resurrecting Ydersius, their decapitated god. His headless body still thrashes about, mindless, in the Darklands, waiting to be reunited with his lost skull. Serpentfolk numbers are so small that reclaiming their dominance seems a distant dream, especially since their reproduction is slow. Though a parent can birth a dozen young at once, the gestation period lasts up to a decade, and the likelihood that even one will be zyss is low. There's no telling whether a child will be zyss or aapoph, regardless of parentage. A coveted zyss child is just as likely to arise from aapoph parents as from two zyss, and every serpentfolk colony has someone in charge of sorting the young, identifying the earliest signs of magic in them.

```statblock
creature: "Coil Spy"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
