---
type: creature
group: ["Angel", "Celestial"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Ninkonda"
level: "17"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Angel"
trait_02: "Celestial"
trait_03: "Holy"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+29; [[Darkvision]], [[Truesight]] (precise) 30 feet"
languages: "Common, Empyrean (Truespeech)"
skills:
  - name: Skills
    desc: "Acrobatics +27, Athletics +34, Diplomacy +34, Intimidation +30, Religion +28, Society +26"
abilityMods: ["+9", "+4", "+7", "+3", "+6", "+7"]
abilities_top: []
armorclass:
  - name: AC
    desc: "39; **Fort** +30, **Ref** +27, **Will** +33"
health:
  - name: HP
    desc: "350; **Weaknesses** unholy 15"
abilities_mid:
  - name: "Aura of Refection"
    desc: "60 feet. The ninkonda's mirror refects the weaknesses in creatures' souls. A creature that enters or starts its turn in the aura must succeed at a DC 36 [[Will]] save or be [[Dazzled]] and take a –2 penalty to Will saves against the ninkonda's abilities for 1 round. <br>  <br> > [!danger] Effect: Aura of Reflection"
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Refect Spell"
    desc: "`pf2:r` **Trigger** The ninkonda is targeted by a ranged spell attack <br>  <br> **Effect** The ninkonda attempts to refect the spell with the mirror in their armor. They gain a +4 circumstance bonus to AC against the triggering attack. If the attack misses, the spell is refected back at the caster, who must roll a second ranged spell attack against their own AC to determine if the spell hits them instead."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Nailed Fist +34 (`pf2:1`) (agile, holy, magical, versatile p), **Damage** 2d8 piercing plus 2d6+17 bludgeoning"
  - name: "Ranged strike"
    desc: "Nail Blast +34 (`pf2:1`) (holy, magical), **Damage** 3d8+8 piercing plus 2d8 bleed"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 38, attack +30<br>**8th** [[Pinpoint]]<br>**7th** [[Interplanar Teleport (self only)]]<br>**6th** [[Truesight]] (Constant)<br>**5th** [[Truespeech]], [[Truespeech]] (Constant)<br>**3rd** [[Ring of Truth]] (At Will)<br>**1st** [[Divine Lance]], [[Light]]"
abilities_bot:
  - name: "Nail Barrage"
    desc: "`pf2:2` The ninkonda sprays a mass of nails that deal @Damage[14d8[piercing]|options:area-damage] damage in a @Template[type:emanation|distance:20] with a DC 38 [[Reflex]] save. They can't use Nail Barrage again for 1d4 rounds."
  - name: "Soul Reflection"
    desc: "`pf2:1` The ninkonda aims the mirror in their armor at a creature [[Dazzled]] by their aura of refection to force the creature to gaze upon its past sins. The creature must succeed at a DC 38 [[Will]] save or become [[Slowed]] 1 for 1 round as it refects upon its actions (or 1 minute on a critical failure, as the creature's actions continue to weigh on it). A holy creature or a morally upstanding creature (as determined by the GM) uses the outcome that is one degree of success better than it rolled on its save. A creature that fails its save is then temporarily immune to Soul Refection for 1 minute."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

When once-honorable mortals fall to wickedness and perform terrible atrocities, ninkondas set out to track them down. Clad in plate armor that features a brilliantly shining mirror in the chest and bearing spikes and nails impaled into their bodies, ninkondas serve as hunters for celestial forces. Rather than immediately slaying their quarries, however, ninkondas do their best to encourage a change of heart and foster eventual redemption in their targets. Ninkondas use their mirrors to refect the sins of the target and showcase the state of their soul, and many targets seek to change after glimpsing this refection. Those who don't soon fnd themselves facing off against the wordless might of their hunter.

```statblock
creature: "Ninkonda"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
