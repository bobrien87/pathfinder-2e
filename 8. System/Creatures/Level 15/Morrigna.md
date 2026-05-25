---
type: creature
group: ["Monitor", "Psychopomp"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Morrigna"
level: "15"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Monitor"
trait_02: "Psychopomp"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+28; [[Darkvision]], [[Lifesense]] (precise) 60 feet"
languages: "Chthonian, Diabolic, Empyrean, Necril, Requian (Speak with Animals, Truespeech)"
skills:
  - name: Skills
    desc: "Athletics +27, Diplomacy +27, Intimidation +29, Religion +29, Society +24, Stealth +27, Boneyard Lore +28"
abilityMods: ["+8", "+4", "+4", "+3", "+6", "+4"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Shepherd's Touch"
    desc: "A morrigna's Strikes affect incorporeal creatures as though etched with a *[[Ghost Touch]]* property rune and deal 4d6 void damage to living creatures or 4d6 vitality damage to undead."
armorclass:
  - name: AC
    desc: "38; **Fort** +25, **Ref** +27, **Will** +29"
health:
  - name: HP
    desc: "240; regeneration 20 (deactivated by acid or fire); **Immunities** death effects, disease; **Resistances** void 15, poison 15"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 20 (Deactivated by Acid or Fire)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Wrappings Lash"
    desc: "`pf2:r` **Trigger** A creature within reach of the morrigna's web wrappings uses an action to Strike or attempt a skill check <br>  <br> **Effect** The morrigna makes a web wrappings Strike against the triggering creature. If the strike is a critical hit, the triggering action is disrupted."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bo Staff +31 (`pf2:1`) (magical, parry, reach 10 ft., trip), **Damage** 2d8+14 bludgeoning plus [[Spirit Touch]]"
  - name: "Melee strike"
    desc: "Web Wrappings +29 (`pf2:1`) (magical, reach 10 ft.), **Damage** 3d12+14 bludgeoning plus [[Grab]] plus [[Spirit Touch]]"
spellcasting:
  - name: "Divine Spontaneous Spells"
    desc: "DC 35, attack +30<br>**6th** (4 slots) [[Field of Life]], [[Spirit Blast]]<br>**5th** (4 slots) [[Scouting Eye]], [[Sending]]<br>**4th** (4 slots) [[Dispelling Globe]], [[Read Omens]], [[Unfettered Movement]]<br>**3rd** (4 slots) [[Blindness]], [[Crisis of Faith]], [[Dream Message]]<br>**2nd** (4 slots) [[Calm]], [[Dispel Magic]], [[See the Unseen]], [[Silence]]<br>**1st** (4 slots) [[Bane]], [[Bless]], [[Detect Magic]], [[Enfeeble]], [[Heal]], [[Read Aura]], [[Stabilize]], [[Vitality Lash]], [[Void Warp]]"
  - name: "Divine Innate Spells"
    desc: "DC 37, attack +29<br>**5th** [[Truespeech]] (Constant)<br>**4th** [[Talking Corpse]]<br>**2nd** [[Speak with Animals]] (Constant)"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` A morrigna can take the appearance of any Small or Medium animal or humanoid. This doesn't change their Speed or their attack and damage modifiers with their Strikes, but it might change the damage type their Strikes deal. Unless they choose to manifest their web wrappings in their new form, they cannot make web wrappings Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Spider Minions"
    desc: "`pf2:3` The morrigna summons a [[Giant Tarantula]] or [[Spider Swarm]]. These spiders have the summoned trait and remain for 10 minutes or until reduced to 0 Hit Points, whichever comes first. The morrigna does not need to Sustain the Spell to direct these summoned creatures, and the morrigna can have any number of summoned spiders in existence at once. The morrigna can see through the eyes of any of their summoned spiders at any time."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Bounty hunters and investigators, morrignas seek out creatures who thwart death or interfere with the natural flow of souls. Morrignas dress in flowing spider silk and wear masks reminiscent of webs, as they consider patient and watchful spiders to be their spiritual kin.

Psychopomps are guardians and shepherds of the dead in the Boneyard, the vast plane of graves where mortal souls are judged and sent on to their eternal rewards or damnations. Psychopomps ensure that the dead come to terms with their transition from mortality and are properly sorted into the appropriate afterlife. They also protect souls from being preyed upon by supernatural predators. Nearly all psychopomps wear masks, especially when they're likely to be interacting with mortals, although the types of masks they wear are as varied as the psychopomps themselves. The courts of the Boneyard preside in Requian, a somber yet melodic language spoken slowly with various tonal shifts.

Many psychopomps are intimately involved with the Boneyard's massive bureaucracy. Few pursue mercy, justice, or personal gain; their duties to Pharasma and her Boneyard are supreme. Nevertheless, individual psychopomps interpret their duties in different ways, which might put them in conflict with mortals or even with each other.

```statblock
creature: "Morrigna"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
