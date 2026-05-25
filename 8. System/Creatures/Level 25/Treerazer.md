---
type: creature
group: ["Amphibious", "Demon"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Treerazer"
level: "25"
rare_01: "Unique"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Amphibious"
trait_02: "Demon"
trait_03: "Fiend"
trait_04: "Unholy"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+46; [[Darkvision]], [[Truesight]] (precise) 60 feet"
languages: "Chthonian, Common, Elven, Fey (Telepathy 300 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +40, Arcana +38, Athletics +45, Intimidation +46, Nature +49, Occultism +38, Religion +45, Stealth +40"
abilityMods: ["+12", "+9", "+11", "+7", "+8", "+8"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Staggering Strike"
    desc: "When Treerazer scores a critical hit with a melee attack, the target is [[Stunned]] 2."
armorclass:
  - name: AC
    desc: "54; **Fort** +42, **Ref** +40, **Will** +43"
health:
  - name: HP
    desc: "550; Regeneration 50 (deactivated by holy); **Immunities** death effects, disease, mental, poison; **Weaknesses** holy 20; **Resistances** acid 20, cold 15, fire 15, physical 20 except cold iron"
abilities_mid:
  - name: "+2 Status to All Saves vs. Magic"
    desc: ""
  - name: "Regeneration 50 (Deactivated by Holy)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Aura of Corruption"
    desc: "120 feet. <br>  <br> Plants near Treerazer twist, deform, and transform into thorny or fungoid parodies of their natural shapes. A living creature in this area must succeed at a DC 47 [[Fortitude]] save each round or become partially transformed into plantlike matter. Those who fail this saving throw are treated as if they were plants for the purposes of any effect that particularly harms or inconveniences plant creatures more than other creatures, but do not gain any benefits of being plant creatures. <br>  <br> This effect lasts as long as the creature remains within the area of corruption and for 1 minute thereafter. <br>  <br> > [!danger] Effect: Aura of Corruption"
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Dispelling Strike"
    desc: "`pf2:0` **Frequency** once per round <br>  <br> **Trigger** Treerazer hits a creature, object, or spell effect with a weapon Strike or subjects one to Defoliation; <br>  <br> **Effect** Treerazer casts his innate [[Dispel Magic]], targeting the creature he hit with his Strike or one spell affecting that creature."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Blackaxe +47 (`pf2:1`) (acid, magical, reach 15 ft., sweep, unholy), **Damage** 5d12+18 slashing plus 1d6 acid"
  - name: "Melee strike"
    desc: "Jaws +45 (`pf2:1`) (agile, magical, reach 15 ft., unarmed, unholy), **Damage** 5d10+20 slashing"
spellcasting:
  - name: "Primal Innate Spells"
    desc: "DC 49, attack +43<br>**10th** [[Freeze Time]]<br>**8th** [[Desiccate]]<br>**6th** [[Tangling Creepers]] (At Will), [[Truesight]] (Constant)<br>**4th** [[Unfettered Movement]] (Constant)<br>**3rd** [[Earthbind]] (At Will), [[Wall of Thorns]]<br>**2nd** [[Dispel Magic]] (At Will), [[Telekinetic Maneuver]] (At Will)<br>**1st** [[Telekinetic Projectile]]"
abilities_bot:
  - name: "Blackaxe - Owner's Authority"
    desc: "`pf2:1` **Requirements** Treerazer isn't wielding *Blackaxe*. <br>  <br> **Effect** Treerazer sense the world around Blackaxe as though you were in its location and can use any of your innate spells through the link as if it were the source of the spell. If another creature is wielding Blackaxe, it must succeed at a DC 50 [[Will]] save or be [[Slowed]] 2 until it relinquishes the weapon."
  - name: "Blackaxe - Owner's Reclamation"
    desc: "`pf2:0` **Requirements** Treerazer isn't wielding *Blackaxe*. <br>  <br> **Effect** *Blackaxe* appears in Treerazer's hands, teleporting instantly from its prior location."
  - name: "Blackaxe - Rejuvenating Deforestation"
    desc: "`pf2:1` **Frequency** once per minute. <br>  <br> **Effect** Make a Strike against a living tree with Blackaxe. If it hits, the tree withers to ash and you heal 250 Hit Points and gain the benefit of a 6th-rank [[Sound Body]] spell."
  - name: "Defoliation"
    desc: "`pf2:2` Treerazer exudes a pulse of sickly green light in a 30-foot-radius emanation. All plants in the area (including creatures under the effect of his aura of corruption) blacken and wither. <br>  <br> Non-creature plants immediately wither and die. Plant and fungus creatures take 20d8 void damage with a DC 49 [[Fortitude]] save. A creature that fails its save is [[Doomed]] 1 for 1 minute and [[Sickened]] 3. <br>  <br> Treerazer can choose to exclude any number of plants or fungi in the area from this effect, and generally does so to preserve twisted and corrupted plants or fungi, or plant and fungus creatures that are allied to his cause. <br>  <br> Treerazer can't use Defoliation for 1d4 rounds."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Treerazer, the self-styled Lord of the Blasted Tarn, is a powerful demon on the cusp of ascending to the true power of one of the rulers of the Abyss itself-a demon lord. For now, even as a nascent demon lord, Treerazer is a dangerous foe.

Treerazer rarely leaves his swampy realm of Tanglebriar-a large thicket of tainted foliage and rotting detritus just south of Kyonin's Fierani Forest-but can be encountered anywhere within that toxic mire, often accompanied by a small legion of demons, corrupted fey, and other deadly allies. Certain occult rituals have the power to call him forth from Tanglebriar, granting him the opportunity to directly work his evils beyond the realm to which he has been exiled. Some believe that no eldritch force contains Treerazer and that, were he willing, he could travel Golarion with impunity, spreading the twisted blessings of his touch and the corruption of his presence, yet the Lord of the Blasted Tarn is as cunning and canny as he is deadly, and prefers to work his evils on the world from the safety of his nightmare realm.

```statblock
creature: "Treerazer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
