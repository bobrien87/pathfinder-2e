---
type: creature
group: ["Azata", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Raelis"
level: "11"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Azata"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: "Common, Diabolic, Draconic, Empyrean (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +21, Arcana +19, Athletics +19, Deception +20, Occultism +19, Performance +22, Religion +20, Society +21, Stealth +19"
abilityMods: ["+6", "+6", "+5", "+4", "+3", "+5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "30; **Fort** +21, **Ref** +24, **Will** +18"
health:
  - name: HP
    desc: "200; **Weaknesses** cold iron 10, unholy 10"
abilities_mid:
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +23 (`pf2:1`) (agile, finesse, holy, magical), **Damage** 2d6+9 bludgeoning plus [[Improved Grab]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 30, attack +22<br>**6th** [[Vibrant Pattern]], [[Zealous Conviction]]<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Outcast's Curse]], [[Unfettered Movement]], [[Unfettered Movement]] (Constant)<br>**3rd** [[Enthrall]], [[Heroism]], [[Lightning Bolt]], [[Veil of Privacy]] (Constant)<br>**1st** [[Bless]], [[Detect Magic]], [[Divine Lance]], [[Figment]], [[Haunting Hymn]], [[Read Aura]], [[Telekinetic Projectile]]"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The raelis can take on the appearance of any Small or Medium humanoid, or any Medium or smaller animal. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but might change the damage type their Strikes deal. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Recount Epic"
    desc: "`pf2:2` The raelis recounts a tale to inspire their allies to heroic feats. For the next minute, all allied creatures who heard the epic gain a +1 circumstance bonus to Acrobatics, Athletics, and Performance checks. <br>  <br> > [!danger] Effect: Recount Epic"
  - name: "Siphon Scroll"
    desc: "`pf2:2` The raelis Casts a Spell from a scroll within 60 feet that they've read with Word Caller; this scroll must be divine. If this spell has the holy or vitality trait, they Cast it as one spell rank higher. This expends the scroll as normal."
  - name: "Word Caller"
    desc: "`pf2:1` The raelis senses the presence of words around them within 60 feet, reading up to 100 pages of nonmagical writing or automatically succeeding at a [[Recall Knowledge]] to identify 1 magical scroll."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Formed from the souls of storytellers, these boisterous azatas roam the planes, seeking out ever more impressive stories to collect. They attempt to spread joy by sharing these tales and righting wrongs they encounter. Their constant search for tales brings raelises to the mortal Universe more often than other azatas.

A raelis is generally knowledgeable about trails and directions, as their journeys take them to a variety of different locales. Raelises prefer to avoid taking the same journey twice and will go out of their way to avoid doing so. After millennia of constant journeys, a raelis becomes a living atlas, something they take great pride in.

Raelises adore brawling and wrestling, and often travel in mortal guises so as not to unduly infuence the events they chronicle. Their ability to travel discreetly among settlements make raelises excellent spies and discreet agents for gods with similar interests.

```statblock
creature: "Raelis"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
