---
type: creature
group: ["Amphibious", "Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nuckelavee"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Amphibious"
trait_02: "Fey"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Low-Light Vision]]"
languages: "Aklo, Common, Fey"
skills:
  - name: Skills
    desc: "Athletics +19, Intimidation +19, Nature +16, Stealth +18, Survival +16"
abilityMods: ["+6", "+3", "+4", "+1", "+3", "+4"]
abilities_top:
  - name: "Mortasheen"
    desc: "The target can't recover from the fatigued condition caused by mortasheen until the disease is cured. Mortasheen gains the virulent trait against animals and plants <br>  <br> **Saving Throw** DC 28 [[Fortitude]] save <br>  <br> **Stage 1** Carrier with no ill effect (1 day); <br>  <br> **Stage 2** [[Drained]] 1 and [[Fatigued]] (1 day) <br>  <br> **Stage 3** [[Drained]] 2 and fatigued (1 day) <br>  <br> **Stage 4** dead"
armorclass:
  - name: AC
    desc: "28; **Fort** +19, **Ref** +16, **Will** +20"
health:
  - name: HP
    desc: "190; **Immunities** disease, poison; **Weaknesses** cold iron 10"
abilities_mid:
  - name: "Frightful Presence"
    desc: "30 feet. DC 25 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Purity Vulnerability"
    desc: "Unpolluted fresh water burns a nuckelavee like acid, dealing 1d6 acid damage to it and causing it to be [[Sickened]] 2. <br>  <br> A nuckelavee can't heal from damage when it's in an area that isn't polluted (subject to GM discretion)."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Bastard Sword +21 (`pf2:1`) (magical, reach 10 ft., two hand d12), **Damage** 2d8+12 slashing plus 1d6 poison plus [[Mortasheen]]"
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (agile, unarmed), **Damage** 2d8+12 piercing plus 1d6 poison plus [[Mortasheen]]"
  - name: "Melee strike"
    desc: "Hoof +20 (`pf2:1`), **Damage** 2d6+12 bludgeoning plus [[Mortasheen]]"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 28, attack +20<br>**5th** [[Control Water]]<br>**3rd** [[Aqueous Orb]]"
abilities_bot:
  - name: "Blight Breath"
    desc: "`pf2:2` The nuckelavee breathes a @Template[cone|distance:30] of foulness, dealing @Damage[8d6[void]|options:area-damage] damage to living creatures in the area with a DC 28 [[Fortitude]] save. A creature that fails also takes @Damage[2d6[bleed]|options:area-damage] damage. <br>  <br> The nuckelavee can't use Blight Breath again for 1d4 rounds."
  - name: "Trample"
    desc: "`pf2:3` Medium or smaller, hoof, DC 28 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

When pollution despoils a natural waterway, it draws the dreaded nuckelavee to it from the First World. This spirit of wrath is a grisly sight to behold: a horselike monstrosity with the gnarled upper body of a humanoid growing directly from its back. Further enhancing its awfulness, not a patch of skin exists on the misshapen hybrid form, as though it survived its own flaying.

When a nuckelavee rides forth from its domain, it wreaks a trail of destruction across the land surrounding its path. Nuckelavees are considered among the cruelest and most monstrous fey, seen by some as just desserts visited upon those who would befoul the waters of their homes. A nuckelavee, however, doesn't discriminate between those who pollute and those who merely have the misfortune to be in the wrong place at the wrong time.

Despite their vile reputation among humanoids, nuckelavees are generally respectful of their fey counterparts. Once pollution has been cleansed and water fey like naiads return to a body of water, nuckelavees will peacefully withdraw.

```statblock
creature: "Nuckelavee"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
